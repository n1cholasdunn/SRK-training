import { useEffect, useState } from 'react';
import useProfile from '../hooks/useProfile';
import { TOKEN_KEY } from '../api';
import { Test } from '../types/test';

const SingleTest = () => {
  const token = localStorage.getItem(TOKEN_KEY);
  const { data: profile } = useProfile();
  const [testData, setTestData] = useState<Test | null>(null);
  useEffect(() => {
    if (profile) {
      fetch(`http://127.0.0.1:8000/training/tests/health-markers/33/`, {
        headers: {
          Authorization: `Token ${token}`,
        },
        method: 'GET',
      })
        .then(response => response.json())
        .then(data => {
          setTestData(data);
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    }
  }, [token, profile]);
  console.log(testData);

  // TODO modify to take in the id of the item rendered in so it deletes the proper one
  const handleDelete = async () => {
    if (profile) {
      fetch(`http://127.0.0.1:8000/training/tests/health-markers/delete/32/`, {
        headers: {
          Authorization: `Token ${token}`,
        },
        method: 'DELETE',
      })
        .then(response => response.json())
        .then(data => {
          console.log(data.message);
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    }
  };
  return (
    <>
      <div>Test # {'33'}</div>
      <div>
        <h1>...</h1>
        {testData ? (
          <>
            <div>{testData.weight}</div>
            <div>{testData.bmi}</div>
            <div>{testData.waist_hip_ratio}</div>
            <div>{testData.resting_hr}</div>
            <div>{testData.blood_pressure}</div>
            <div>{testData.vo2_max}</div>
            <button onClick={handleDelete}>🗑️</button>
          </>
        ) : (
          <div>Something went wrong</div>
        )}
      </div>
    </>
  );
};

export default SingleTest;
