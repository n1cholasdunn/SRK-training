import { useEffect, useState } from 'react';
import { TOKEN_KEY } from '../api';
import useProfile from '../hooks/useProfile';
import { Test } from '../types/test';

const AssessmentList = () => {
  const token = localStorage.getItem(TOKEN_KEY);
  const { data: profile } = useProfile();
  const [testData, setTestData] = useState<Test[] | null>(null);
  useEffect(() => {
    if (profile) {
      fetch(
        `http://127.0.0.1:8000/training/assessments/health-markers/${profile.id}/`,
        {
          headers: {
            Authorization: `Token ${token}`,
          },
          method: 'GET',
        }
      )
        .then(response => response.json())
        .then(data => {
          setTestData(data[0].tests);
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    }
  }, [token, profile]);
  return (
    <>
      <div>AssessmentList of User {profile?.id}</div>
      {testData?.map(test => (
        <>
          <div>
            <h1>...</h1>
            <div>{test.weight}</div>
            <div>{test.bmi}</div>
            <div>{test.waist_hip_ratio}</div>
            <div>{test.resting_hr}</div>
            <div>{test.blood_pressure}</div>
            <div>{test.vo2_max}</div>
          </div>
        </>
      ))}
    </>
  );
};

export default AssessmentList;
