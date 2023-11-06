import {Outlet} from 'react-router-dom';
import Header from '../ui/Header';

const RootLayout = () => {
  return (
    <div className=" bg-gray-50 text-gray-950 relative pt-28 sm:pt-36 ">
      <Header />
      <main>
        <Outlet />
      </main>
    </div>
  );
};

export default RootLayout;
