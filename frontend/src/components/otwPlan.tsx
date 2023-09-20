import { useEffect } from 'react';
// import { fetchOTWPlan } from '../gsheets/fetch';
import { TOKEN_KEY } from '../api';

const OtwPlan = () => {
  const token = localStorage.getItem(TOKEN_KEY);
  useEffect(() => {
    fetch('http://127.0.0.1:8000/training/plans/otw/create/', {
      headers: {
        Authorization: `Token ${token}`,
      },
      method: 'POST',
    })
      .then(response => response.json())
      .then(data => {
        console.log(data.message); // "Data inputted successfully!"
      })
      .catch(error => {
        console.error('There was an error!', error);
      });
  }, [token]);
  return <div>otwPlan</div>;
};

export default OtwPlan;
