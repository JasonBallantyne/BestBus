import GoogleDirections from "../../components/GoogleDirections";

function PlannerTab() {

  return(
    <div>

      <h1>Plan your route</h1>
      <p>Enter an origin and destination and we will find the best route using public transport</p>
      <br/>

      <GoogleDirections />

    </div>
  )
}

export default PlannerTab;