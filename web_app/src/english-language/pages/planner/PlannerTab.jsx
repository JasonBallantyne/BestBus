import GoogleDirections from "../../components/GoogleDirections";

function PlannerTab() {

  const container = {
    margin: "4rem 0 0 0"
  };
  const feature = {
    margin: "5rem auto",
    width: "70%",
    minWidth: "700px",
    padding: "3rem 0",
    backgroundColor: '#fbc31c',
    borderRadius: "1rem",
  };

  return(
    <div style={container}>

      <div style={feature}>
        <h1>Plan your route</h1>
        <p>Enter an origin and destination and we will find the best route using public transport</p>
        <br/>
        <GoogleDirections />
      </div>

    </div>
  )
}

export default PlannerTab;