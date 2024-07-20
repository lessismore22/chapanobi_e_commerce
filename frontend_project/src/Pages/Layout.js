import { Outlet } from "react-router-dom";
import Navbar from '../Components/Navbar/Navbar'
import Footer from "../Components/Footer/Footer";

function Layout() {
    // const location = useLocation();
    // const noNavbarPaths = ["/login", "/register"];

    return (
		<>
			<Navbar />
            {/* {!noNavbarPaths.includes(location.pathname) && <Navbar />} */}
            <Outlet />
            <Footer />
        </>
    );
}

export default Layout;
