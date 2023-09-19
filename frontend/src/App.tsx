// import { useEffect } from 'react';
// import useGoogleAuthToken from './hooks/useGoogleAuthToken';
// import useGoogleAuthLink from './hooks/useGoogleAuthLink';
// import useProfile from './hooks/useProfile';
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import HomePage from './components/HomePage';
import OtwPlan from './components/otwPlan';

function App() {
  // const { data: profile, refetch: fetchProfile } = useProfile();
  // const { data: googleAuth, refetch: fetchGoogleAuth } = useGoogleAuthLink();
  // const { mutate, isSuccess } = useGoogleAuthToken();

  // useEffect(() => {
  //   if (googleAuth) {
  //     window.location.replace(googleAuth.authorizationUrl);
  //   }
  // }, [googleAuth]);

  // useEffect(() => {
  //   const searchParams = new URLSearchParams(document.location.search);

  //   const code = searchParams.get('code');
  //   const state = searchParams.get('state');

  //   if (code && state) {
  //     mutate({ code, state });
  //   }
  // }, [mutate]);

  // useEffect(() => {
  //   if (isSuccess) {
  //     fetchProfile();
  //   }
  // }, [isSuccess, fetchProfile]);

  // useEffect(() => {
  //   if (googleAuth) {
  //     window.location.replace(googleAuth.authorizationUrl);
  //   }
  // }, [googleAuth]);

  // const handleGoogleLogin = () => {
  //   fetchGoogleAuth();
  // };

  return (
    <Router>
      <div className='App'>
        <Routes>
          <Route
            path='/'
            element={<HomePage />}
          />
          <Route
            path='/training/input-otw-plan/'
            element={<OtwPlan />}
          />
          {/* <div>
            {profile ? (
              <h1>Hello {profile.firstName}!</h1>
            ) : (
              <button onClick={handleGoogleLogin}>Login with Google</button>
            )}
            <Link to={'/otw-plan'}>
              <div>CLICK FOR OTW PLAN CREATION</div>
            </Link>
          </div> */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
