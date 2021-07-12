import GoogleMapReact from 'google-map-react';
import MapPin from "./MapPin"

const GOOGLE_API_KEY = process.env.REACT_APP_GOOGLE_API_KEY;

export default function SimpleMap(){
  const defaultProps = {
    center: {
      lat: 53.34,
      lng: -6.26
    },
    zoom: 11
  };

  return (
    <div style={{ height: '100%', width: '100%' }}>
      <GoogleMapReact
        bootstrapURLKeys={{ key: GOOGLE_API_KEY }}
        defaultCenter={defaultProps.center}
        defaultZoom={defaultProps.zoom}
      >
        <MapPin 
          lat={53.34}
          lng={-6.26}
          name="dublin center"
        />
      </GoogleMapReact>
    </div>
  );
}