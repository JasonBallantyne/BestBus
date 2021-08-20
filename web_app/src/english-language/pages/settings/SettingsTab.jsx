import Dropdown from 'react-bootstrap/Dropdown';

function SettingsTab() {
  const container = {
    margin: "4rem 0 0 0",
  };
  const feature = {
    margin: "4rem 0",
  };
  function changeLanguage() {
    localStorage.setItem('language', '/ga-ie')
  };
  return(
    <div style={container}>
      <div style={feature}>
        <h3>Choose Language:</h3>
        <p>Choose between English or Gaeilge</p>
        <Dropdown>
          <Dropdown.Toggle id="dropdown-button-dark-example1" variant="secondary">
            Language
          </Dropdown.Toggle>

          <Dropdown.Menu variant="dark">
            <Dropdown.Item active>English</Dropdown.Item>
            <Dropdown.Item onClick={changeLanguage()} href="/ga-ie">Gaeilge</Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      </div>
      <div style={feature}>
        <h3>Install app:</h3>
        <p>For ease of use, we suggest installing this app on your device for better performance and ease of accessibility.</p>
        <p>To make this possible, this app is a PWA (progressive web app). Go to your browser settings and click the option "Install Best Bus".</p>
        <p>Unfortunately, some browsers and devices do not support this feature.</p>
      </div>
    </div>

  )
}

export default SettingsTab;