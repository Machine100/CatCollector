import React from 'react';
import './App.css';
import AddItems from './components/additems';
import RemoveItems from './components/removeitems';
import DisplayWorld from './components/displayworld';
import GenerateWorld from './components/generateworld';

function App() {
  return (
    <div>
      <GenerateWorld/>
      <AddItems/>
      <DisplayWorld/>
      <RemoveItems/>
    </div>
  );
}

export default App;
