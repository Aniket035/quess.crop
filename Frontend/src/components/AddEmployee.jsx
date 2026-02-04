import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const AddEmployee = () => {
  const [formData, setFormData] = useState({ employee_id: '', full_name: '', email: '', department: '' });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await axios.post('/employees/', formData);
      navigate('/');
    } catch (err) {
      setError(err.response?.data?.detail || 'Error adding employee');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h2>Add Employee</h2>
      <form className="form" onSubmit={handleSubmit}>
        <input className="input" name="employee_id" placeholder="Employee ID" onChange={handleChange} required />
        <input className="input" name="full_name" placeholder="Full Name" onChange={handleChange} required />
        <input className="input" name="email" type="email" placeholder="Email" onChange={handleChange} required />
        <input className="input" name="department" placeholder="Department" onChange={handleChange} required />
        <div className="row">
          <button className="btn" type="submit" disabled={loading}>{loading ? 'Adding...' : 'Add'}</button>
        </div>
        {error && <p className="error">{error}</p>}
      </form>
    </div>
  );
};

export default AddEmployee;