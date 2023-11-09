import {useEffect} from 'react';
import useGoogleAuthToken from '../../hooks/useGoogleAuthToken';
import useGoogleAuthLink from '../../hooks/useGoogleAuthLink';
import useProfile from '../../hooks/useProfile';
import AboutMe from '../../components/AboutMe';
import Intro from '../../components/Intro';
import SectionDivider from '../../components/ui/SectionDivider';
import Coaching from '../../components/Coaching';
import {BsGoogle} from 'react-icons/bs';
import Contact from '../../components/Contact';
import {useUserPerms} from '../../hooks/useUserPerms';

const HomePage = () => {
  const {data: profile, refetch: fetchProfile} = useProfile();
  const {data: googleAuth, refetch: fetchGoogleAuth} = useGoogleAuthLink();
  const {mutate, isSuccess} = useGoogleAuthToken();

  const {data: perms, isLoading, isError, error} = useUserPerms();
  // const isSuperUser = data?.isSuperuser;
  useEffect(() => {
    console.log(perms, 'USER PERMS');
  });
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
      mutate({code, state});
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
    <main className="flex flex-col items-center px-4">
      {profile ? (
        <h1>Hello {profile.firstName}!</h1>
      ) : (
        <button onClick={handleGoogleLogin}>
          Sign In <BsGoogle />
        </button>
      )}
      <Intro />
      <SectionDivider />
      <AboutMe />
      <Coaching />
      <Contact />
    </main>
  );
};

export default HomePage;
