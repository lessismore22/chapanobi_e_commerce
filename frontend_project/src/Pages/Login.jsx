import React, { useState } from "react";
import "./LoginRegister.css";
import { Link, useNavigate } from "react-router-dom";

const Login = () => {
	const navigate = useNavigate()
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    // const toggleMode = () => {
    //     setEmail("");
    //     setPassword("");
	// };
	const handleLogin = (e) => {
		e.preventDefault()
		console.log("Logged in")
		console.log(password, email)
		navigate('/')
	}

    return (
		<div className="form">
			<div className="logo">

			</div>
            <div className="login-signup-container">
                <h1>Welcome, Login to Get Started</h1>
                <form onSubmit={handleLogin}>
                    <div className="form-group">
                        <label htmlFor="email">Email:</label>
                        <input
                            type="email"
							id="email"
							placeholder="Enter Email"
							name="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="password">Password:</label>
                        <input
                            type="password"
                            id="password"
							value={password}
							placeholder="Enter Password"
							name="password"
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>

                    <button type="submit">Login</button>
                </form>
                <p className="mt-3">
                    Don't have an account?
                    <Link className=" text-red-500 italic" to="/register">
                        Register
                    </Link>
                </p>
            </div>
        </div>
    );
};

export default Login;
