import UserDropdown from "../../components/UserDropdown"
import GoogleMap from "../../components/GoogleMap"

function RealtimeTab() {
  const content = {
    display: "grid",
    margin: "5rem 3rem",
    gridTemplateRows: "1fr 2fr"
  };
  const dropdownsContainer = {
    background: "lightgrey",
    gridColumnStart: "1",
    gridColumnEnd: "2",
    margin: "3rem",
    display: "grid",
    gridTemplateColumns: "1fr 1fr"
  };
  const userdropdownContainer  = {
    margin: "3rem"
  };
  const stopdropdownContainer  = {
    margin: "3rem"
  };
  const mapContainer = {
    background: "lightgrey",
    gridColumnStart: "1",
    gridColumnEnd: "2",
    margin: "0 3rem"
  };
  return(
    <div>
      <div style={content}>
        <div style={dropdownsContainer}>
          <div style={userdropdownContainer}>
            <UserDropdown />
          </div>
          <div style={stopdropdownContainer}>
            <UserDropdown />
          </div>
        </div>
        <div style={mapContainer}>
          <GoogleMap />
        </div>
      </div>
    </div>
  )
}

export default RealtimeTab;