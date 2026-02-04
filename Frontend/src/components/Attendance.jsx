import { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const Attendance = () => {
  const { id } = useParams();
  const [attendances, setAttendances] = useState([]);
  const [formData, setFormData] = useState({ date: '', status: 'Present' });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchAttendance = async () => {
      try {
        const res = await axios.get(`/employees/${id}/attendance/`);
        setAttendances(res.data);
      } catch (err) {
        setError('Error fetching attendance');
      } finally {
        setLoading(false);
      }
    };
    fetchAttendance();
  }, [id]);

  const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(`/employees/${id}/attendance/`, formData);
      setAttendances([...attendances, res.data]);
    } catch (err) {
      setError('Error marking attendance');
    }
  };

  if (loading) return <p>Loading...</p>;
  if (error) return <p className="error">{error}</p>;

  return (
    <div className="container">
      <h2>Attendance for Employee {id}</h2>
      <form className="form-inline" onSubmit={handleSubmit}>
        <input className="input" name="date" type="date" onChange={handleChange} required />
        <select className="input" name="status" onChange={handleChange}>
          <option>Present</option>
          <option>Absent</option>
        </select>
        <button className="btn" type="submit">Mark</button>
      </form>
      {attendances.length ? (
        <table className="table">
          <thead><tr><th>Date</th><th>Status</th></tr></thead>
          <tbody>{attendances.map(att => <tr key={att.id}><td>{att.date}</td><td>{att.status}</td></tr>)}</tbody>
        </table>
      ) : <p>No attendance records.</p>}
    </div>
  );
};

export default Attendance;