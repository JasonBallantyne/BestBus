import { useQuery, gql } from "@apollo/client";
import { useContext, useState, useEffect } from "react";
import { StationsContext } from "../contexts/stations";
import CloseButton from 'react-bootstrap/CloseButton';
import ListGroup from 'react-bootstrap/ListGroup';

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
    minWidth: "15rem",
  };
  const input = {
    width: "13vw",
    margin: "1rem 1rem 1rem 0"
  };
  const item = {
    display: "grid",
    gridTemplateColumns: "10fr 1fr"
  };
  const favourite = {
    backgroundColor: "#4992bb"
  };
  const removeButton = {
    padding: "0.7rem",
    marginRight: "-3rem"
  };

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return (
    <div style={container}>
      <h3>Search By Stop</h3>
      <input  style={input} type="text" placeholder="stop number" onChange={event => {setStopSearch(event.target.value)}} />
      <ListGroup>
        {favourites.map((stop) => {
          return (
            <div style={item} key={"favdiv-" + stop.stopNum}><ListGroup.Item style={favourite} action onClick={() => {chooseStop(stop)}}>{stop.stopNum}</ListGroup.Item><CloseButton style={removeButton} onClick={() => {removeFromStopFavourites(stop)}}></CloseButton></div>
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
            <div style={item} key={stop.stopNum}><ListGroup.Item action onClick={() => {chooseStop(stop)}}>{stop.stopNum}</ListGroup.Item></div>
          )
        })}
      </ListGroup>
    </div>
  )
}

export default StopsDropdown;