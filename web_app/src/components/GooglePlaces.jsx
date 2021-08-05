import React, { useState } from 'react';
import GooglePlacesAutocomplete from 'react-google-places-autocomplete';

export default function GooglePlaces() {

  // states for origin and deestination values 
  const [origin, setOrigin] = useState(null);
  const [destination, setDestination] = useState(null);

  // styles for origin and destination search elements
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

  // function triggered when origin and destination selected
  function calcRoute() {
    console.log(origin)
    console.log(destination)
  }

  return (
    <div style={routeChoiceContainer}>
      <div style={placesDropdown}>
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
      <button style={chooseRouteButton} onClick={calcRoute}>Calculate Route</button>
    </div>
  );
}