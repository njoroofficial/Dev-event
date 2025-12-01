# 🚀 Dev-Event Hub

A modern, full-featured developer event management platform built with React and Vite. Discover, book, and manage tech conferences, hackathons, meetups, and workshops all in one place.

![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-7-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-4-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![JSON Server](https://img.shields.io/badge/JSON_Server-REST_API-green?style=for-the-badge)

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Environment Variables](#-environment-variables)
- [API Endpoints](#-api-endpoints)
- [Pages & Routes](#-pages--routes)
- [Authentication](#-authentication)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🎫 For Attendees

- **Browse Events** - Discover upcoming developer events with detailed information including date, time, location, and agenda
- **Event Details** - View comprehensive event information including overview, description, organizer details, and tags
- **Book Events** - Secure your spot with an easy-to-use booking form
- **Email Confirmation** - Receive booking confirmations via EmailJS integration
- **Manage Bookings** - View and cancel your event bookings from a personal dashboard

### 👨‍💼 For Administrators

- **Event Management Dashboard** - Full CRUD operations for events
- **Add Events** - Create new events with comprehensive details (title, image, location, venue, date, time, mode, audience, description, tags, and more)
- **Edit Events** - Modify existing event information through a user-friendly modal form
- **Delete Events** - Remove events with confirmation dialogs and optimistic UI updates
- **Track Bookings** - Monitor booked spots for each event

### 🎨 User Experience

- **Modern UI** - Beautiful glassmorphism design with gradient accents
- **Responsive Design** - Fully responsive layout that works seamlessly on all devices
- **Interactive Animations** - Custom light ray effects and smooth transitions
- **Real-time Updates** - Optimistic UI updates for better user experience

---

## 🛠 Tech Stack

### Frontend

| Technology             | Purpose                                 |
| ---------------------- | --------------------------------------- |
| **React 19**           | UI library with latest features         |
| **Vite 7**             | Fast build tool and dev server          |
| **React Router DOM 7** | Client-side routing                     |
| **TailwindCSS 4**      | Utility-first CSS framework             |
| **Lucide React**       | Beautiful icon library                  |
| **EmailJS**            | Email service for booking confirmations |
| **Three.js / OGL**     | 3D graphics for visual effects          |

### Backend

| Technology      | Purpose                 |
| --------------- | ----------------------- |
| **JSON Server** | RESTful API mock server |

### Dev Tools

| Technology         | Purpose             |
| ------------------ | ------------------- |
| **ESLint**         | Code linting        |
| **tw-animate-css** | Animation utilities |

---

## 📁 Project Structure

```
Dev-event/
├── public/
│   ├── icons/          # App icons (logo, UI icons)
│   └── images/         # Event images
├── src/
│   ├── assets/         # Static assets
│   ├── components/     # Reusable UI components
│   │   ├── ui/         # Base UI components (button, etc.)
│   │   ├── BookEvent.jsx
│   │   ├── BookingCard.jsx
│   │   ├── EventCard.jsx
│   │   ├── EventContent.jsx
│   │   ├── EventList.jsx
│   │   ├── NavBar.jsx
│   │   ├── LightRays.jsx
│   │   └── ...
│   ├── lib/            # Utilities and context
│   │   ├── auth-context.jsx  # Authentication context
│   │   ├── constant.js
│   │   └── utils.js
│   ├── pages/          # Page components
│   │   ├── AdminDashboard.jsx
│   │   ├── EventPage.jsx
│   │   ├── HomePage.jsx
│   │   ├── LandingPage.jsx
│   │   ├── ManageBookings.jsx
│   │   ├── SignIn.jsx
│   │   └── SignUp.jsx
│   ├── App.jsx         # Main app component with routes
│   ├── main.jsx        # App entry point
│   └── index.css       # Global styles
├── dev-event-api/
│   ├── db.json         # JSON Server database
│   └── package.json
├── package.json
├── vite.config.js
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- **Node.js** (v18 or higher recommended)
- **npm** or **yarn**

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/njoroofficial/Dev-event.git
   cd Dev-event
   ```

2. **Install frontend dependencies**

   ```bash
   npm install
   ```

3. **Install API dependencies**
   ```bash
   cd dev-event-api
   npm install
   cd ..
   ```

### Running the Application

You'll need to run both the API server and the frontend development server.

1. **Start the JSON Server (API)**

   ```bash
   cd dev-event-api
   npm start
   ```

   The API will be available at `http://localhost:3000`

2. **Start the Frontend (in a new terminal)**
   ```bash
   npm run dev
   ```
   The application will be available at `http://localhost:5173`

### Build for Production

```bash
npm run build
```

The build output will be in the `dist/` directory.

### Preview Production Build

```bash
npm run preview
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
# API URL (optional - defaults to http://localhost:3000)
VITE_API_URL=http://localhost:3000
```

---

## 📡 API Endpoints

The JSON Server provides the following RESTful endpoints:

### Events

| Method   | Endpoint             | Description            |
| -------- | -------------------- | ---------------------- |
| `GET`    | `/events`            | Get all events         |
| `GET`    | `/events/:id`        | Get single event by ID |
| `GET`    | `/events?slug=:slug` | Get event by slug      |
| `POST`   | `/events`            | Create new event       |
| `PUT`    | `/events/:id`        | Update event           |
| `DELETE` | `/events/:id`        | Delete event           |

### Users

| Method | Endpoint              | Description              |
| ------ | --------------------- | ------------------------ |
| `GET`  | `/users`              | Get all users            |
| `GET`  | `/users?email=:email` | Get user by email        |
| `POST` | `/users`              | Create new user (signup) |

### Bookings

| Method   | Endpoint               | Description         |
| -------- | ---------------------- | ------------------- |
| `GET`    | `/bookings?userId=:id` | Get user's bookings |
| `POST`   | `/bookings`            | Create new booking  |
| `DELETE` | `/bookings/:id`        | Cancel booking      |

---

## 🗺 Pages & Routes

| Route           | Component        | Description             | Access        |
| --------------- | ---------------- | ----------------------- | ------------- |
| `/`             | `LandingPage`    | Marketing landing page  | Public        |
| `/home`         | `HomePage`       | Browse all events       | Public        |
| `/events/:slug` | `EventPage`      | Event details & booking | Public        |
| `/signin`       | `SignIn`         | User login              | Public        |
| `/signup`       | `SignUp`         | User registration       | Public        |
| `/bookings`     | `ManageBookings` | User's bookings         | Authenticated |
| `/admin`        | `AdminDashboard` | Event management        | Admin only    |

---

## 🔑 Authentication

The application uses a simple authentication system with React Context:

### User Roles

- **Regular Users**: Can browse events, book events, and manage their bookings
- **Admin Users**: Full access including event CRUD operations

### Admin Access

To access the admin dashboard, sign in with:

- **Email**: `admin@gmail.com`
- **Password**: (set during signup or in db.json)

### How It Works

1. User credentials are stored in `db.json` via JSON Server
2. Authentication state is managed with React Context (`AuthProvider`)
3. User session persists via `localStorage`

>

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ for the developer community
</p>
