import { Link } from "react-router-dom";

const NavBar = () => {
  return (
    <header>
      <nav>
        <Link to="/" className="logo">
          <img
            src="../../public/icons/logo.png"
            alt="logo"
            width={24}
            height={24}
          />
          <p>Dev-Event Hub</p>
        </Link>

        <ul>
          <Link to="/">Home</Link>
          <Link to="/events">Events</Link>
          <Link to="/events/new">Create Events</Link>
        </ul>
      </nav>
    </header>
  );
};

export default NavBar;
