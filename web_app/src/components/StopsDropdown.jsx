import { useQuery, gql } from "@apollo/client";
import { useContext, useState, useEffect } from "react";
import { StationsContext } from "../contexts/stations";
import CloseButton from 'react-bootstrap/CloseButton';
import { MdDelete } from "react-icons/md";

const STOPS = gql`
  query {
    uniqueStops {
        stopName
        stopNum
        latitude
        longitude
    }
  }
`;

function  StopsDropdown() {

  const { loading, error, data } = useQuery(STOPS);
  const [stopSearch, setStopSearch] = useState('');

  const [, dispatch ] = useContext(StationsContext);

  const [favourites, setFavourites] = useState([]);
  const [updateFavourites, setUpdateFavourites] = useState(false);

  useEffect(() => {
    setFavourites(getStopFavourites())
    setUpdateFavourites(false)
  }, [updateFavourites])

  // fucntion to get the stop favourites from local storage
  function getStopFavourites() {
    return JSON.parse(localStorage.getItem('stop-favourites') || '[]')
  };

  // function adds stop to favourites array in local storage, removes oldest if array larger than 3
  function addToStopFavourites(item) {
    let favourites = getStopFavourites();
    let include = true;
    favourites.forEach((i) => {
      if (i.stopNum === item.stopNum) {
        include = false;
      }
    })
    if (include) {
      favourites.push(item)
    }
    while (favourites.length > 3) {
      favourites.shift()
    }
    localStorage.setItem('stop-favourites', JSON.stringify(favourites));
    setUpdateFavourites(true)
  };

  // function to remove a given stop from favourites in local storage
  function removeFromStopFavourites(item) {
    let favourites = JSON.parse(localStorage.getItem('stop-favourites') || '[]');
    let counter = 0;
    let index = 0;
    favourites.forEach((i) => {
      if (i.stopNum === item.stopNum) {
        index = counter;
      }
      counter++;
    })
    if (index < favourites.length) {
      favourites.splice(index, 1);
    }
    localStorage.setItem('stop-favourites', JSON.stringify(favourites));
    setUpdateFavourites(true)
  };

  // this function is fired each time a stop button is selected
  function chooseStop(stop) {
    addToStopFavourites(stop);
    dispatch({type: "update_stations", payload: [stop]})
  };

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
      <h3>Choose a Stop</h3>
      <input type="text" placeholder="Search by stop number" onChange={event => {setStopSearch(event.target.value)}} />
      <div style={buttonContainer}>
        {favourites.map((stop) => {
          return (
            <div style={favouriteDiv} key={"favdiv-" + stop.stopNum}><input type="button" style={favouritesButton} key={"favinput-" + stop.stopNum} value={stop.stopNum} onClick={ () => {chooseStop(stop)}}></input><CloseButton onClick={() => {removeFromStopFavourites(stop)}} style={removeButton}><MdDelete/></CloseButton></div>
          )
        })}
        { data.uniqueStops.filter((val)=> {
          if (stopSearch === "") {
            return val
          } else if (val.stopNum.startsWith(stopSearch)) {
            return val
          } else {
            return null
          }
        }).slice(0, 8-favourites.length).map((stop) => {
          return (
            <input type="button" style={button} key={stop.stopNum} value={stop.stopNum} onClick={ () => {chooseStop(stop)}}></input>
          )
        })}
      </div>
    </div>
  )
}

export default StopsDropdown;