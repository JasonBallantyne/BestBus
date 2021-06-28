import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import RealtimeTab from './RealtimeTab'
import PlannerTab from './PlannerTab'
import SettingsTab from './SettingsTab'

function Menu() {
  return (
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
  )
}

export default Menu;