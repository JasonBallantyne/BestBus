import './App.css';
import React, { Component } from 'react';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import RealtimeTab from './pages/realtime/RealtimeTab'
import RealtimeTabMobile from './pages/realtime/RealtimeTabMobile.jsx'
import PlannerTab from './pages/planner/PlannerTab'
import SettingsTab from './pages/settings/SettingsTab'
class App extends Component {
  constructor(props) {
    super(props)
    this.state = { matches: window.matchMedia("(min-width: 1000px)").matches };
  }

  componentDidMount() {
    const handler = e => this.setState({matches: e.matches});
    window.matchMedia("(min-width: 1000px)").addEventListener("change", (handler));
  }
  render() {
    return (
      <div >
      {this.state.matches && (
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
      {!this.state.matches && (
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
}

export default App;