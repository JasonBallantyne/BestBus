import { useQuery, gql } from "@apollo/client";
import { useContext, useState } from "react";
import { StationsContext } from "../contexts/stations";

const ROUTES = gql`
  query {
    uniqueRoutes {
        routeNum
        direction
        destination
        longitudes
        latitudes
        names
        stops
        names
    }
  }
`;

function  RoutesDropdown() {

  const { loading, error, data } = useQuery(ROUTES);
  const [routeSearch, setRouteSearch] = useState('');

  const [, dispatch ] = useContext(StationsContext);

  function chooseRoute(route) {
    // get all required gtfs_data split out
    let stopNums = route.stops.split(",");
    let stopNames = route.names.split(",");
    let latitudes = route.latitudes.split(",");
    let longitudes = route.longitudes.split(",");

    // new array to store organised gtfs_data
    let routeOrganised = [];

    // iterate through gtfs_data and add to organised list
    for (let i = 0; i < stopNums.length; i++) {
      let newStop = {"routeNum": route.routeNum, "direction": route.direction, "stopName": stopNames[i].trim(), "stopNum": stopNums[i].trim(), "latitude": latitudes[i].trim(), "longitude": longitudes[i].trim()};
      routeOrganised.push(newStop)
      // console.log(newStop)
    }
    dispatch({type: "update_stations", payload: [routeOrganised]})
  }

  const container = {
    width: "13vw",
    minWidth: "11rem",
  }
  const buttonContainer = {
    height: "10rem"
  };
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
        { data.uniqueRoutes.filter((val)=> {
          if (routeSearch === "") {
            return val
          } else if (val.routeNum.toLowerCase().startsWith(routeSearch.toLowerCase())) {
            return val
          } else {
            return null
          }
        }).slice(0, 8).map((route) => {
          return (
            <input type="button" style={button} key={route.routeNum + "-" + route.direction} value={route.routeNum + " (" + route.direction + ")"} onClick={ () => {chooseRoute(route)}}></input>
          )
        })}
      </div>
    </div>
  )
}

export default RoutesDropdown;