import { useQuery, gql } from "@apollo/client";
import { useContext, useState } from "react";
import { StationsContext } from "../contexts/stations";

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

  function chooseStop(stop) {
    dispatch({type: "update_stations", payload: [stop]})
  };

  const container = {
    width: "13vw",
    minWidth: "11rem",
    height: "400px"
  };
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
      <h3>Choose a Stop</h3>
      <input type="text" placeholder="Search by stop number" onChange={event => {setStopSearch(event.target.value)}} />
      <div style={buttonContainer}>
        { data.uniqueStops.filter((val)=> {
          if (stopSearch === "") {
            return val
          } else if (val.stopNum.startsWith(stopSearch)) {
            return val
          } else {
            return null
          }
        }).slice(0, 8).map((stop) => {
          return (
            <input type="button" style={button} key={stop.stopNum} value={stop.stopNum} onClick={ () => {chooseStop(stop)}}></input>
          )
        })}
      </div>
    </div>
  )
}

export default StopsDropdown;