import { useState, useRef } from 'react';
import GooglePlacesAutocomplete from 'react-google-places-autocomplete';
import { GoogleMap, DirectionsRenderer, DirectionsService } from '@react-google-maps/api';

// styles for places origin and destination search elements
const routeChoiceContainer = {
  margin: "0 0 0 3rem",
  display: "grid",
  gridTemplateColumns: "2fr 2fr 1fr"
};
const placesDropdown = {
  margin: "0 1rem",
};
const chooseRouteButton = {
  margin: "0 2rem",
};

// style for map
const containerStyle = {
  height: "50rem",
  margin: "3rem 5rem"
};

// position of map
const center = {
  lat: 53.34,
  lng: -6.26
};

// an empty place object, to be used as placeholder
const emtpyPlaceObj = {
  "label": null,
  "value": {
      "description": null,
      "place_id": null,
  }
};



export default function GoogleDirections() {

  // states for origin and destination values 
  const [origin, setOrigin] = useState(emtpyPlaceObj);
  const [destination, setDestination] = useState(emtpyPlaceObj);

  // states for directions components
  const [dirService, setDirService] = useState(<div></div>);
  const [dirRender, setDirRender] = useState(<div></div>);

  // state for render count (otherwise @react-google-maps/api library has a problem with infinitley rendering)
  let count = useRef(0);

  // directions service options
  const DirectionsServiceOption = {
    destination: { placeId: destination.value.place_id },
    origin: { placeId: origin.value.place_id },
    travelMode: "TRANSIT",
  };

  // directions callback which renders the directions on map or console logs error
  const directionsCallback = (response) => {
    if (response !== null && origin !== null && count.current < 2) {
      if (response.status === "OK") {
        count.current += 1;
        setDirRender(
          <DirectionsRenderer
            options={{
              directions: response,
            }}
          />
        );
      } else {
        count.current = 0;
        console.log("response: ", response);
      }
    }
  };

  // function triggered when 'calculate route' button clicked
  function calcRoute() {
    if (origin !== null && destination !== null) {
      setDirService(
        <DirectionsService
          options={DirectionsServiceOption}
          callback={directionsCallback}
        />
      );
      count.current = 0;
    };
  };

  return (
    <div>
      <div style={routeChoiceContainer}>
        <div style={placesDropdown}>
          {/* palces autocomplete for choosing origin */}
          <GooglePlacesAutocomplete
            apiOptions={{ language: 'en-GB', region: 'ie' }}
            selectProps={{
              origin,
              onChange: setOrigin,
            }}
            autocompletionRequest={{
              bounds: [
                { lat: 53.66814524847642, lng: -6.713710391817202 },
                { lat: 53.11900451404619, lng: -5.971729440309045 }
              ],
              componentRestrictions: {
              country: ['ie'],
              }
            }}
          />
        </div>    
        <div style={placesDropdown}>
          {/* places autocomplete for choosing destination */}
          <GooglePlacesAutocomplete
            apiOptions={{ language: 'en-GB', region: 'ie' }}
            selectProps={{
              destination,
              onChange: setDestination,
            }}
            autocompletionRequest={{
              bounds: [
                { lat: 53.66814524847642, lng: -6.713710391817202 },
                { lat: 53.11900451404619, lng: -5.971729440309045 }
              ],
              componentRestrictions: {
              country: ['ie'],
              }
            }}
          />
        </div>
        <button style={chooseRouteButton} onClick={calcRoute}>Ríomh Slí</button>
      </div>
      {/* Map component */}
      <GoogleMap
        mapContainerStyle={containerStyle}
        center={center}
        zoom={10}
      >
        {/* directions components are dynamically rendered here */}
        <div>
          {dirRender}
          {dirService}
        </div>
      </GoogleMap>
    </div>
  )
};