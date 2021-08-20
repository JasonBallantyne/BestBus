import StopsDropdown from "../../components/StopsDropdown"
import RoutesDropdown from "../../components/RoutesDropdown"
import GoogleMap from "../../components/GoogleMap"
import { StationsProvider } from "../../contexts/stations"

function RealtimeTab() {
  const content = {
    display: "grid",
    margin: "5rem 3rem",
    gridTemplateRows: "1fr 1fr"
  };
  const dropdownsContainer = {
    gridColumnStart: "1",
    gridColumnEnd: "2",
    margin: "3rem",
    display: "grid",
    gridTemplateColumns: "1fr 1fr",
    height: "550px",
    borderRadius: "1rem",
    backgroundColor: "#fbc31c"
  };
  const stopsDropdownContainer  = {
    margin: "3rem 5rem"
  };
  const routesDropdownContainer  = {
    margin: "3rem"
  };
  const mapContainer = {
    gridColumnStart: "1",
    gridColumnEnd: "2",
    margin: "0 3rem",
    height: "700px"
  };
  return(
    <StationsProvider>
      <div style={content}>
        <div style={mapContainer}>
          <GoogleMap />
        </div>
        <div style={dropdownsContainer}>
          <div style={stopsDropdownContainer}>
            <StopsDropdown />
          </div>
          <div style={routesDropdownContainer}>
            <RoutesDropdown />
          </div>
        </div>
      </div>
    </StationsProvider>
  )
}

export default RealtimeTab;