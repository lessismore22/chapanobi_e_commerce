import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './Components/Navbar/Navbar';
import Home from './Pages/Home';
import About from './Pages/About';
import Contact from './Pages/Contact';
import LoginSignup from './Pages/LoginSignup';
import Footer from './Components/Footer/Footer';
// import React, { useState, useEffect } from React


 function App() {

//     Const [data, setData] = useState([{}])

//     useEffect(() => {
//       fetch('/api/users/register')
//         .then(response => response.json())
//         .then(data => setUsers(data))
//         .catch(error => console.error('Error fetching data:', error));
//     }, []);



  return (
    <div>

      <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/About' element={<About/>} />
        <Route path='Contact' element={<Contact/>} />
        <Route path='/' element={<product/>}/>
            <Route path=':productId' element={<product/>}/>
        <Route/>
        <Route path='/cart' element={<cart/>}/>
        <Route path='/Login' element={<LoginSignup/>}/>
      </Routes>
        <Footer />
      </BrowserRouter>
      </div>
  );
}

export default App;
