import { useEffect } from 'react';
import useGoogleAuthToken from '../../hooks/useGoogleAuthToken';
import useGoogleAuthLink from '../../hooks/useGoogleAuthLink';
import useProfile from '../../hooks/useProfile';
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
      <Link to={'/training/assessments/shark-skills/create/'}>
        <div>CLICK FOR Shark skills CREATION</div>
      </Link>
      <div>...</div>
      <Link to={'/training/plans/otw/1/'}>
        <div>CLICK TO GET OTW PLAN </div>
      </Link>
      <div>...</div>
      <Link to={'/training/plans/gym/create/'}>
        <div>CLICK FOR gym PLAN CREATION</div>
      </Link>
      <div>...</div>
      <Link to={'/training/plans/gym/1/'}>
        <div>CLICK TO GET gym PLAN </div>
      </Link>
      <div>...</div>
      <Link to={'/training/plans/prehab/create/'}>
        <div>CLICK FOR prehab PLAN CREATION</div>
      </Link>
      <div>...</div>
      <Link to={'/training/plans/prehab/1/'}>
        <div>CLICK TO GET prehab PLAN </div>
      </Link>
      <div>...</div>
      <Link to={'/training/tests/health-markers/33/'}>
        <div>CLICK TO GET test with id 33 </div>
      </Link>
      <div>...</div>
      <Link to={'/training/assessments/health-markers/3/'}>
        <div>CLICK TO GET assessments for user 3 </div>
      </Link>
      <div>...</div>
      {/* <Link to={'/training/tests/shark-skills/create/'}>
        <div>CLICK TO Create shark skills test </div>
      </Link>
      <div>...</div> */}
      <Link to={'/training/assessments/health-markers/create/'}>
        <div>CLICK TO create health markers plan</div>
      </Link>
      <Link to={'/username/update/availability/'}>
        <div>UPDATE AVAILABILITY</div>
      </Link>
      <div>...</div>)
    </div>
  );
};

export default HomePage;
