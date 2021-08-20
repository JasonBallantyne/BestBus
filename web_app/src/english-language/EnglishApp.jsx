import React, { useEffect, useState } from 'react';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import RealtimeTab from './pages/realtime/RealtimeTab'
import RealtimeTabMobile from './pages/realtime/RealtimeTabMobile.jsx'
import PlannerTab from './pages/planner/PlannerTab'
import SettingsTab from './pages/settings/SettingsTab'
import logo from '../images/icon.png'

export default function EnglishApp(props) {

  const { passedState } = props;

  console.log(logo);

  useEffect(() => {
    localStorage.setItem('language', '/en-ie')
  }, []);

  const [state, setState] = useState(passedState);

  useEffect(() => {
    const handler = e => setState({matches: e.matches});
    window.matchMedia("(min-width: 1000px)").addEventListener("change", (handler));
  }, [state]);

  const header = {
    width: "40%",
    height: "6rem",
    margin: "2rem auto 3rem auto",
    position: "relative",
    gridTemplateColumns: "1fr 1fr"
  };
   const headerItems = {
     height: "4.5rem"
   };
  
  return (
    <div>
    {state.matches && (
      <div className="App">
        <header className="App-header" style={header}>
          <img src={logo} alt="Logo" style={headerItems}/>
          <h1 style={headerItems}>Best Bus</h1>
        </header>
        <Tabs>
          <TabList>
            <Tab>Realtime</Tab>
            <Tab>Journey Planner</Tab>
            <Tab>Settings</Tab>
          </TabList>
  
          <TabPanel>
            <RealtimeTab />
          </TabPanel>
          <TabPanel>
            <PlannerTab />
          </TabPanel>
          <TabPanel>
            <SettingsTab />
          </TabPanel>
        </Tabs>
      </div>
    )}
    {!state.matches && (
      <div className="App">
        <header className="App-header" style={header}>
          <img src={logo} alt="Logo" style={headerItems}/>
          <h1 style={headerItems}>Best Bus</h1>
        </header>
        <Tabs>
          <TabList>
            <Tab>Realtime</Tab>
            <Tab>Journey Planner</Tab>
            <Tab>Settings</Tab>
          </TabList>
  
          <TabPanel>
            <RealtimeTabMobile />
          </TabPanel>
          <TabPanel>
            <PlannerTab />
          </TabPanel>
          <TabPanel>
            <SettingsTab />
          </TabPanel>
        </Tabs>
      </div>
    )}
    </div>
  );
  
}