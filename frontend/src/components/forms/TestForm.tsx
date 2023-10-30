import { useState, FormEvent } from 'react';
import { TOKEN_KEY } from '../../api';

const GSheetForm = () => {
  const [url, setUrl] = useState('');
  const token = localStorage.getItem(TOKEN_KEY);
  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    console.log(url);

    try {
      const response = await fetch(
        'http://127.0.0.1:8000/training/assessments/health-markers/create/',
        {
          method: 'POST',
          headers: {
            Authorization: `Token ${token}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ url }), // Sends the URL to the backend
        }
      );

      if (response.ok) {
        const responseBody = await response.json();
        console.log('Form submitted successfully', responseBody);
      } else {
        console.error('Failed to submit the form', response);
      }
    } catch (error) {
      console.error('Failed to submit the form', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        URL:
        <input
          type='url'
          value={url}
          onChange={e => setUrl(e.target.value)}
          required
        />
      </label>
      <button type='submit'>Submit</button>
    </form>
  );
};

export default GSheetForm;
