import { useQuery, gql } from "@apollo/client";
import { useContext, useState, useEffect } from "react";
import { StationsContext } from "../contexts/stations";
import CloseButton from 'react-bootstrap/CloseButton';
import { MdDelete } from "react-icons/md";

const ROUTES = gql`
  query {
    uniqueRoutes {
        id
        lineId
        direction
        destination
        longitudes
        latitudes
        names
        stops
        gachAinm
        firstDepartureSchedule
    }
  }
`;

function  RoutesDropdown() {

  const { loading, error, data } = useQuery(ROUTES);
  const [routeSearch, setRouteSearch] = useState('');

  const [favourites, setFavourites] = useState([]);
  const [updateFavourites, setUpdateFavourites] = useState(false);

  useEffect(() => {
    setFavourites(getRouteFavourites())
    setUpdateFavourites(false)
  }, [updateFavourites])

  // function setFavourites(favs) {
  //   localStorage.setItem('favourites', JSON.stringify(favs));
  // }

  // fucntion to get the route favourites from local storage
  function getRouteFavourites() {
    return JSON.parse(localStorage.getItem('route-favourites') || '[]')
  };

  // function adds route to favourites array in local storage, removes oldest if array larger than 3
  function addToRouteFavourites(item) {
    let favourites = JSON.parse(localStorage.getItem('route-favourites') || '[]');
    let include = true;
    favourites.forEach((i) => {
      if (i.id === item.id) {
        include = false;
      }
    })
    if (include) {
      favourites.push(item)
    }
    while (favourites.length > 3) {
      favourites.shift()
    }
    localStorage.setItem('route-favourites', JSON.stringify(favourites));
    setUpdateFavourites(true)
  };

  // function to remove a given route from favourites in local storage
  function removeFromRouteFavourites(item) {
    let favourites = JSON.parse(localStorage.getItem('route-favourites') || '[]');
    let counter = 0;
    let index = 0;
    favourites.forEach((i) => {
      if (i.id === item.id) {
        index = counter;
      }
      counter++;
    })
    if (index < favourites.length) {
      favourites.splice(index, 1);
    }
    localStorage.setItem('route-favourites', JSON.stringify(favourites));
    setUpdateFavourites(true)
  };

  const [, dispatch ] = useContext(StationsContext);

  // this function is fired each time a route button is selected
  function chooseRoute(route) {

    addToRouteFavourites(route)

    // get all required gtfs_data split out
    let stopNums = route.stops.split(",");
    let stopNames = route.names.split(",");
    let latitudes = route.latitudes.split(",");
    let longitudes = route.longitudes.split(",");
    let irishNames = route.gachAinm.split(",");

    // new array to store organised gtfs_data
    let routeOrganised = [];

    // iterate through gtfs_data and add to organised list
    for (let i = 0; i < stopNums.length; i++) {
      let newStop = {"lineId": route.lineId, "direction": route.direction, "destination": route.destination,
      "longitude": longitudes[i].trim(), "latitude": latitudes[i].trim(), "stopName": stopNames[i].trim(), "stopNum": stopNums[i].trim(),
      "irishName": irishNames[i].trim(), "departureSchedule": route.firstDepartureSchedule};
      routeOrganised.push(newStop)
    }

    // console.log(routeOrganised)

    dispatch({type: "update_stations", payload: [routeOrganised]})
  }

  const container = {
    width: "13vw",
    minWidth: "11rem",
  };
  const buttonContainer = {
    height: "10rem"
  };
  const favouriteDiv = {
    display: "grid",
    gridTemplateColumns: "5fr 1fr"
  };
  const favouritesButton = {
    display: "block",
    width: "100%",
    height: "2rem",
    margin: "3% 0",
    backgroundColor: "grey"
  };
  const removeButton = {
    height: "2rem",
    margin: "14% 0"
  }
  const button = {
    display: "block",
    width: "100%",
    height: "2rem",
    margin: "3% 0"
  };

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return (
    <div style={container}>
      <h3>Choose a Route</h3>
      <input type="text" placeholder="Search by route number" onChange={event => {setRouteSearch(event.target.value)}} />
      <div style={buttonContainer}>
        {favourites.map((route) => {
          return (
            <div style={favouriteDiv} key={"favdiv-" + route.lineId + "-" + route.direction}><input type="button" style={favouritesButton} key={"favinput-" + route.lineId + "-" + route.direction} value={route.lineId + " (" + route.direction + ")"} onClick={ () => {chooseRoute(route)}}></input><CloseButton onClick={() => {removeFromRouteFavourites(route)}} style={removeButton}><MdDelete/></CloseButton></div>
          )
        })}
        { data.uniqueRoutes.filter((val)=> {
          if (routeSearch === "") {
            return val
          } else if (val.lineId.toLowerCase().startsWith(routeSearch.toLowerCase())) {
            return val
          } else {
            return null
          }
        }).slice(0, 8-favourites.length).map((route) => {
          return (
            <input type="button" style={button} key={route.lineId + "-" + route.direction} value={route.lineId + " (" + route.direction + ")"} onClick={ () => {chooseRoute(route)}}></input>
          )
        })}
      </div>
    </div>
  )
}

export default RoutesDropdown;