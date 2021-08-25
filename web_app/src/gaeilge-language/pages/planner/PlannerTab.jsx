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
        <h1>Pleanagaí bhfur turas</h1>
        <p>Cuir isteach tionscnamh agus ceann scríbe agus gheobhaidh muid an bealach is fearr ag úsáid iompar poiblí</p>
        <br/>
        <GoogleDirections />
      </div>
    </div>
  )
}

export default PlannerTab;