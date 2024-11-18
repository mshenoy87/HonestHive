import './App.css';
import { UserInput, AnalysisArea} from './components/components';
import 'bootstrap/dist/css/bootstrap.css';
import React, {useState} from 'react';

function App() {

  const [statement, setStatement] = useState('');

  return (
    <div className="App">
                <h1>Honest Hive</h1>
                <AnalysisArea 
                    statement={statement}
                    className="d-flex align-items-center analysis_area well well-lg"/>
                <UserInput setStatement={setStatement} />
    </div>
  );
}

export default App;
