// import { useEffect } from 'react';
// import useGoogleAuthToken from './hooks/useGoogleAuthToken';
// import useGoogleAuthLink from './hooks/useGoogleAuthLink';
// import useProfile from './hooks/useProfile';
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import HomePage from './pages/Home/HomePage';
import PlanList from './components/PlanList';
import OtwPlan from './components/OtwPlan';
import GymPlan from './components/GymPlan';
import PrehabPlan from './components/PrehabPlan';
import PlanListGym from './components/PlanListGym';
import PlanListPrehab from './components/PlanListPrehab';
import TestForm from './components/form/TestForm';

function App() {
  return (
    <Router>
      <div className='App'>
        <Routes>
          <Route
            path='/'
            element={<HomePage />}
          />
          <Route
            path='/training/plans/otw/create/'
            element={<OtwPlan />}
          />
          <Route
            path='/training/plans/otw/1/'
            element={<PlanList />}
          />
          <Route
            path='/training/plans/gym/create/'
            element={<GymPlan />}
          />
          <Route
            path='/training/plans/gym/1/'
            element={<PlanListGym />}
          />
          <Route
            path='/training/plans/prehab/create/'
            element={<PrehabPlan />}
          />
          <Route
            path='/training/plans/prehab/1/'
            element={<PlanListPrehab />}
          />
          <Route
            path='/training/assessments/health-markers/create/'
            element={<TestForm />}
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
