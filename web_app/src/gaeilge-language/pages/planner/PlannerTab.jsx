import GoogleDirections from "../../components/GoogleDirections";

function PlannerTab() {

  return(
    <div>

      <h1>Pleanagaí bhfur turas</h1>
      <p>Cuir isteach tionscnamh agus ceann scríbe agus gheobhaidh muid an bealach is fearr ag úsáid iompar poiblí</p>
      <br/>

      <GoogleDirections />

    </div>
  )
}

export default PlannerTab;