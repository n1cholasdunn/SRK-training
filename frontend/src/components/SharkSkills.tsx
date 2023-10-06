import { useEffect } from 'react';
import useProfile from '../hooks/useProfile';
import { TOKEN_KEY } from '../api';

const SharkSkills = () => {
  const token = localStorage.getItem(TOKEN_KEY);
  const { data: profile } = useProfile();
  useEffect(() => {
    if (profile) {
      fetch(`http://127.0.0.1:8000/training/tests/shark-skills/create/`, {
        headers: {
          Authorization: `Token ${token}`,
        },
        method: 'POST',
      })
        .then(response => response.json())
        .then(data => {
          console.log(data.message);
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    }
  }, [token, profile]);

  // TODO modify to take in the id of the item rendered in so it deletes the proper one

  return (
    <>
      <div> Create Shark skills test</div>
      <div>
        <h1>...</h1>
      </div>
    </>
  );
};

export default SharkSkills;
