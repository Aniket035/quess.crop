import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import EmployeeList from './components/EmployeeList';
import AddEmployee from './components/AddEmployee';
import Attendance from './components/Attendance';

function App() {
  return (
    <Router>
      <div className="app">
        <header className="app-header">
          <h1>HRMS Lite</h1>
          <nav className="nav">
            <Link to="/">Employees</Link>
            <Link to="/add" className="btn-link">Add Employee</Link>
          </nav>
        </header>
        <Routes>
          <Route path="/" element={<EmployeeList />} />
          <Route path="/add" element={<AddEmployee />} />
          <Route path="/employees/:id/attendance" element={<Attendance />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;