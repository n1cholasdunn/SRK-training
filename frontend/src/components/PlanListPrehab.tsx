import { useEffect } from 'react';
// import { fetchOTWPlan } from '../gsheets/fetch';
import { TOKEN_KEY } from '../api';

const PlanListPrehab = () => {
  const token = localStorage.getItem(TOKEN_KEY);
  useEffect(() => {
    fetch('http://127.0.0.1:8000/training/plans/prehab/1/', {
      headers: {
        Authorization: `Token ${token}`,
      },
      method: 'GET',
    })
      .then(response => response.json())
      .then(data => {
        console.log(data); // "Data inputted successfully!"
      })
      .catch(error => {
        console.error('There was an error!', error);
      });
  }, [token]);
  return <div>This is plan exercise data</div>;
};

export default PlanListPrehab;
