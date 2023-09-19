import { useEffect } from 'react';
import useGoogleAuthToken from '../hooks/useGoogleAuthToken';
import useGoogleAuthLink from '../hooks/useGoogleAuthLink';
import useProfile from '../hooks/useProfile';
import { Link } from 'react-router-dom';

const HomePage = () => {
  const { data: profile, refetch: fetchProfile } = useProfile();
  const { data: googleAuth, refetch: fetchGoogleAuth } = useGoogleAuthLink();
  const { mutate, isSuccess } = useGoogleAuthToken();

  useEffect(() => {
    if (googleAuth) {
      window.location.replace(googleAuth.authorizationUrl);
    }
  }, [googleAuth]);

  useEffect(() => {
    const searchParams = new URLSearchParams(document.location.search);

    const code = searchParams.get('code');
    const state = searchParams.get('state');

    if (code && state) {
      mutate({ code, state });
    }
  }, [mutate]);

  useEffect(() => {
    if (isSuccess) {
      fetchProfile();
    }
  }, [isSuccess, fetchProfile]);

  useEffect(() => {
    if (googleAuth) {
      window.location.replace(googleAuth.authorizationUrl);
    }
  }, [googleAuth]);

  const handleGoogleLogin = () => {
    fetchGoogleAuth();
  };
  return (
    <div>
      {profile ? (
        <h1>Hello {profile.firstName}!</h1>
      ) : (
        <button onClick={handleGoogleLogin}>Login with Google</button>
      )}
      <Link to={'/training/input-otw-plan/'}>
        <div>CLICK FOR OTW PLAN CREATION</div>
      </Link>
      )
    </div>
  );
};

export default HomePage;
