import React, { useEffect, useState } from 'react';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import RealtimeTab from './pages/realtime/RealtimeTab'
import RealtimeTabMobile from './pages/realtime/RealtimeTabMobile.jsx'
import PlannerTab from './pages/planner/PlannerTab'
import SettingsTab from './pages/settings/SettingsTab'

export default function EnglishApp(props) {

  const { passedState } = props;

  useEffect(() => {
    localStorage.setItem('language', '/en-ie')
  }, []);

  const [state, setState] = useState(passedState);

  useEffect(() => {
    const handler = e => setState({matches: e.matches});
    window.matchMedia("(min-width: 1000px)").addEventListener("change", (handler));
  }, [state]);

  const app = {
    marginTop: "4rem"
  };
  const header = {
    marginBottom: "2rem"
  };
  
  return (
    <div style={app}>
    {state.matches && (
      <div className="App">
        <header className="App-header">
          <h1 style={header}>Best Bus</h1>
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
        <header className="App-header">
          <h1>Best Bus</h1>
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