import './App.css';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import RealtimeTab from './pages/RealtimeTab'
import PlannerTab from './pages/PlannerTab'
import SettingsTab from './pages/SettingsTab'

function App() {
  return (
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
  );
}

export default App;
