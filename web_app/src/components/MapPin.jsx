function MapPin(props) {
  const { name, markerColor, openPopup } = props;
  const marker = {
    backgroundColor: markerColor,
    cursor: 'pointer',
    position: "absolute",
    top: "0",
    left: "0",
    width: "18px",
    height: "18px",
    border: "2px solid #fff",
    borderRadius: "100%",
    userSelect: "none",
    transform: "translate(-50%, -50%)"
  };
  var arrow = {
    display: "none",
    width: "0",
    height: "0",
    marginLeft: "-2rem",
    marginTop: "-3.65rem",
    borderLeft: "2rem solid transparent",
    borderRight: "2rem solid transparent",
    borderTop: "3rem solid lightgrey",
    position: "absolute",
    zIndex: "3"
  };
  var boxContainer = {
    display: "none",
    backgroundColor: "lightgrey",
    marginLeft: "-8rem",
    marginTop: "-26rem",
    height: "23rem",
    width: "30rem",
    position: "absolute",
    zIndex: "3"
  };
  const header = {
    paddingTop: "0.5rem",
    fontSize: "1.4rem",
    display: "grid",
    gridTemplateColumns: "5fr 1fr"
  };
  const closeButton = {
    cursor: 'pointer',
  };

  // if openPopup prop is true, then ensure the marker renders with popup open
  if (openPopup) {
    arrow = {
      display: "block",
      width: "0",
      height: "0",
      marginLeft: "-2rem",
      marginTop: "-3.65rem",
      borderLeft: "2rem solid transparent",
      borderRight: "2rem solid transparent",
      borderTop: "3rem solid lightgrey",
      position: "absolute",
      zIndex: "3"
    };
    boxContainer = {
      display: "block",
      backgroundColor: "lightgrey",
      marginLeft: "-8rem",
      marginTop: "-26rem",
      height: "23rem",
      width: "30rem",
      position: "absolute",
      zIndex: "3"
    };
  }

  function togglePopup(n) {
    // this function handles the opening of a popup for the stop clicked

    // close already open popups
    var boxClass = document.getElementsByClassName("boxContainer");
    var arrowClass = document.getElementsByClassName("arrow");
    for (let i = 0; i < boxClass.length; i++) {
      if (boxClass[i].style.display === "block") {
        boxClass[i].style.display = "none";
        arrowClass[i].style.display = "none"
      }
    };

    // open this popup
    var box = document.getElementById(n+"-boxContainer");
    var arrow = document.getElementById(n+"-arrow");
    if (box.style.display === "none") {
      box.style.display = "block";
      arrow.style.display = "block";
    } else {
      box.style.display = "none";
      arrow.style.display = "none";
    }
  }

  return(
    <div>
      <div 
        style={marker}
        onClick={() => togglePopup(name)}
      />
      <div
        style={arrow}
        className={"arrow"}
        id={name+"-arrow"}

      />
      <div 
        style={boxContainer} 
        className={"boxContainer"}
        id={name+"-boxContainer"}
      >
        <div style={header}>
          <h3>{name}</h3>
          <div>
            <p style={closeButton} onClick={() => togglePopup(name)}>X</p>
          </div>
        </div>
        <hr />
        <p>arrival/departure time information here...</p>
      </div>
    </div>
  )
};

export default MapPin;