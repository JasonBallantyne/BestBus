import GoogleMapReact from 'google-map-react';
import MapPinRoute from "./MapPinRoute";
import MapPinStop from "./MapPinStop";
import { useContext } from "react";
import { StationsContext } from "../contexts/stations"

const GOOGLE_API_KEY = process.env.REACT_APP_GOOGLE_API_KEY;

export default function SimpleMap(){
  const defaultProps = {
    center: {
      lat: 53.34,
      lng: -6.26
    },
    zoom: 12
  };

  const [ state ] = useContext(StationsContext)

  var pins = [];
  var title = null;

  const header = {
    position: 'absolute',
    zIndex: '2',
    backgroundColor: 'white',
    marginTop: '2.5rem',
    marginLeft: '5rem',
    borderRadius: '1rem',
    padding: '0 1.5rem'
  };

  function closePopups() {
    // function ot close all popups
    var box = document.getElementsByClassName("boxContainer");
    var arrow = document.getElementsByClassName("arrow");
    for (let i = 0; i < box.length; i++) {
      if (box[i].style.display === "block") {
        box[i].style.display = "none";
        arrow[i].style.display = "none"
      }
    };
  }

  if (state) {
    if (state[0].length > 1) {
      state[0].forEach((stop, idx, array) => {
        if (idx === 0) {
          pins.push(
            <MapPinRoute
              key={stop.stopNum}
              lineId={stop.lineId}
              direction={stop.direction}
              destination={stop.destination}
              lng={stop.longitude}
              lat={stop.latitude}
              stopName={stop.stopName}
              stopNum={stop.stopNum}
              irishName={stop.irishName}
              departureSchedule={stop.departureSchedule}
              markerColor="green"
            />
          )
        } else if (idx === array.length - 1) {
          pins.push(
            <MapPinRoute
              key={stop.stopNum}
              lineId={stop.lineId}
              direction={stop.direction}
              destination={stop.destination}
              lng={stop.longitude}
              lat={stop.latitude}
              stopName={stop.stopName}
              stopNum={stop.stopNum}
              irishName={stop.irishName}
              departureSchedule={stop.departureSchedule}
              markerColor="red"
            />
          )
        } else {
          pins.push(
            <MapPinRoute
              key={stop.stopNum}
              lineId={stop.lineId}
              direction={stop.direction}
              destination={stop.destination}
              lng={stop.longitude}
              lat={stop.latitude}
              stopName={stop.stopName}
              stopNum={stop.stopNum}
              irishName={stop.irishName}
              departureSchedule={stop.departureSchedule}
              markerColor="black"
            />
          )
        }
      });
      title = <div style={header}><h1>Route: {state[0][0].lineId} ({state[0][0].direction})</h1></div>
    } else {
      pins.push(
        <MapPinStop
          key={state[0].stopNum}
          lat={state[0].latitude}
          lng={state[0].longitude}
          stopName={state[0].stopName}
          stopNum={state[0].stopNum}
          irishName={state[0].irishName}
          markerColor={"black"}
          openPopup={true}
        />
      )
      title = <div style={header}><h1>Stop: {state[0].stopNum}</h1></div>
    }
  }

  return (
    <div
      style={{ height: '100%', width: '100%' }}
    >
      {title}
      <GoogleMapReact
        bootstrapURLKeys={{ key: GOOGLE_API_KEY }}
        defaultCenter={defaultProps.center}
        defaultZoom={defaultProps.zoom}
        yesIWantToUseGoogleMapApiInternals
        onClick={() => closePopups()}
      >
        {pins}
      </GoogleMapReact>
    </div>
  );
}