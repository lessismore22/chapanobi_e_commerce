import React, { useState } from 'react'
import  './Navbar.css'
import logo from '../Assets/logo.png'
import cart from '../Assets/cart.png'
import { Link } from 'react-router-dom'


const Navbar = () => {

const [menu,setMenu] = useState("home");

  return (
  <div className='navbar'>
      <div className='nav-logo'>
	      <img src={logo} alt="Logo" />
      </div>

    <ul className='nav-menu'>
      <li onClick={()=>{setMenu("home")}}><Link style={{ textDecoration: 'none' }} to='/'>Home</Link>{menu==="home"?<hr/>:<></>}</li>
      <li onClick={()=>{setMenu("about")}}><Link style={{ textDecoration: 'none' }} to='/About'>About</Link>{menu==="about"?<hr/>:<></>}</li>
      <li onClick={()=>{setMenu("contact")}}><Link style={{ textDecoration: 'none' }} to='Contact'>Contact</Link>{menu==="contact"?<hr/>:<></>}</li>
    </ul>

    <div className='nav-login-cart'>
      <div className='btn'><Link to='/login'><button>Login </button></Link></div>
      <div className='btn'><Link to='/register'><button>Register </button></Link></div>
      <div><Link to='/cart'><img src={cart} alt="" /></Link></div>
      <div className='nav-cart-count'>0</div>

    </div>
  </div>



  )
}

export default Navbar;
