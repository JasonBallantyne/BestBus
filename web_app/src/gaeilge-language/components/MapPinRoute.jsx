import { useQuery, gql } from "@apollo/client";
import CloseButton from 'react-bootstrap/CloseButton';

const PREDICTIONS = gql`
  query Prediction ($lineId: String!, $direction: String!, $day: String!, $hour: String!, $minute: String!, $month: String!) {
    prediction (route:$lineId, direction:$direction, day:$day, hour:$hour, minute:$minute month:$month, listSize: 10)
  }
`;

export default function MapPin(props) {

  const { lineId, direction, ceannScribe, irishName, stopNum, markerColor, openPopup } = props;

  const table = {
    border: '1px solid #4992bb',
    borderCollapse: 'collapse',
    margin: '0 0 0 3rem'
  };

  const tableHeader = {
    backgroundColor: '#4992bb',
    color: 'black',
    padding: '0.4rem 3.8rem 0.6rem 0.7rem',
    textAlign: 'left',
    whiteSpace: 'nowrap'
  };

  const items = {
    backgroundColor: 'white',
    border: '1px solid #4992bb',
    padding: '0.25rem 3.8rem 0.4rem 1rem',
    textAlign: 'left',
    whiteSpace: 'nowrap'
  };

  let today = new Date();
  let day = String(today.getDay()-1);
  let hour = String(today.getHours());
  let minute = String(today.getMinutes());
  let month = String(today.getMonth()+1);

  const { loading, error, data } = useQuery(PREDICTIONS, {
    variables: { lineId, direction, day, hour, minute, month },
  });

  let prediction = [];

  if (loading) {
    prediction = "Loading..."
  }
  if (error) {
    prediction = "Error :("
  } 
  if (data) {
    // first the string returned has to be maniupulated to turn into an array
    let predictionString = data.prediction.replace(new RegExp("'", 'g'), "\"");
    let predictionObject = JSON.parse(predictionString);
    prediction = predictionObject[stopNum]
  }

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
    borderTop: "3rem solid #fbc31c",
    position: "absolute",
    zIndex: "3"
  };
  var boxContainer = {
    display: "none",
    marginLeft: "-8rem",
    marginTop: "-28rem",
    height: "25rem",
    width: "30rem",
    position: "absolute",
    zIndex: "3",
    borderRadius: "20px",
    backgroundColor: "#fbc31c"
  };
  const header = {
    padding: "2rem 0 1rem 0",
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
      borderTop: "3rem solid #fbc31c",
      position: "absolute",
      zIndex: "3"
    };
    boxContainer = {
      display: "block",
      marginLeft: "-8rem",
      marginTop: "-28rem",
      height: "25rem",
      width: "30rem",
      position: "absolute",
      zIndex: "3",
      borderRadius: "20px",
      backgroundColor: "#fbc31c"
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
        onClick={() => togglePopup(irishName)}
      />
      <div
        style={arrow}
        className={"arrow"}
        id={irishName+"-arrow"}

      />
      <div 
        style={boxContainer} 
        className={"boxContainer"}
        id={irishName+"-boxContainer"}
      >
        <div style={header}>
          <h3>{irishName}, {stopNum}</h3>
          <div>
          <CloseButton style={closeButton} onClick={() => togglePopup(irishName)}></CloseButton>
          </div>
        </div>
        {data
          ? <table style={table}>
              <thead>
                <tr>
                  <th style={tableHeader}>Ceann Scríbe</th>
                  <th style={tableHeader}>Meastachán Ama</th>
                </tr>
              </thead>
              <tbody>
                {prediction.map((val) => (
                  <tr key={ceannScribe+val}>
                    <td style={items}>{ceannScribe}</td>
                    <td style={items}>{val}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          : <div>{prediction}</div>
        }
      </div>
    </div>
  )
};