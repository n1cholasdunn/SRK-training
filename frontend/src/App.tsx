import './App.css';
import {Route, BrowserRouter as Router, Routes} from 'react-router-dom';
import HomePage from './pages/Home/HomePage';
import PlanList from './components/PlanList';
import OtwPlan from './components/OtwPlan';
import GymPlan from './components/GymPlan';
import PrehabPlan from './components/PrehabPlan';
import PlanListGym from './components/PlanListGym';
import PlanListPrehab from './components/PlanListPrehab';
import TestForm from './components/forms/TestForm';
import AssessmentList from './components/AssessmentList';
import SingleTest from './components/HealthMarkersTest';
import ClientAvailabilityForm from './components/forms/ClientAvailabilityForm';
import ClientInfoForm from './components/forms/ClientInfoForm';
import ClientProgramForm from './components/forms/ClientProgramForm';
import ClientEquipmentForm from './components/forms/ClientEquipmentForm';
import ClimbingAssessmentForm from './components/forms/ClimbingAssessmentForm';

function App() {
  return (
    <Router>
      <div className="App h-full w-full">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route
            path="/training/assessments/shark-skills/create/"
            element={<OtwPlan />}
          />
          <Route path="/training/plans/otw/1/" element={<PlanList />} />
          <Route path="/training/plans/gym/create/" element={<GymPlan />} />
          <Route path="/training/plans/gym/1/" element={<PlanListGym />} />
          <Route
            path="/training/plans/prehab/create/"
            element={<PrehabPlan />}
          />
          <Route
            path="/training/plans/prehab/1/"
            element={<PlanListPrehab />}
          />
          <Route
            path="/training/assessments/health-markers/create/"
            element={<TestForm />}
          />
          <Route
            path="/training/assessments/health-markers/3/"
            element={<AssessmentList />}
          />
          <Route
            path="/training/tests/health-markers/33/"
            element={<SingleTest />}
          />
          <Route
            path="/username/update/availability/"
            element={<ClientAvailabilityForm />}
          />
          {/* TODO create a container component for all of the client forms */}
          <Route path="/username/info/update/" element={<ClientInfoForm />} />
          <Route
            path="/username/program/update/"
            element={<ClientProgramForm />}
          />
          <Route
            path="/username/equipment/update/"
            element={<ClientEquipmentForm />}
          />
          <Route
            path="/climbing/assesments/"
            element={<ClimbingAssessmentForm />}
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
