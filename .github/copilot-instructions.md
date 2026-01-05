# Dev-Event Hub - AI Coding Instructions

## Architecture Overview

React 19 + Vite 7 event management platform with JSON Server backend. Follows a **page-component-context** pattern:

- **Pages** (`src/pages/`) - Route-level components handling layout and data orchestration
- **Components** (`src/components/`) - Reusable UI pieces, `ui/` contains shadcn/ui primitives
- **Context** (`src/lib/auth-context.jsx`) - Global auth state via React Context + localStorage
- **API** - JSON Server at `http://localhost:3000` serving `data/db.json`

## Key Conventions

### Path Aliases

Use `@/` alias for all `src/` imports:

```javascript
import { useAuth } from "@/lib/auth-context";
import BookingCard from "@/components/BookingCard";
```

### Styling

- **TailwindCSS 4** with custom CSS variables in `src/index.css`
- Primary accent: `#5dfeca` / `--primary: #59deca`
- Custom utilities: `flex-center`, `text-gradient`
- shadcn/ui components use JSX (not TSX) - see `components.json`

### Data Fetching Pattern

Components fetch directly from JSON Server:

```javascript
useEffect(() => {
  fetch("http://localhost:3000/events")
    .then((res) => res.json())
    .then(setData)
    .catch(setError)
    .finally(() => setLoading(false));
}, [dependency]);
```

### Optimistic UI Updates

CRUD operations use optimistic updates with rollback (see `AdminDashboard.jsx`, `ManageBookings.jsx`):

```javascript
const previous = [...items];
setItems(prev => prev.filter(i => i.id !== id));
try { await fetch(...) } catch { setItems(previous); }
```

### Authentication

- Context provides: `currentUser`, `login`, `signup`, `logout`, `isAuthenticated`
- Admin check: `currentUser?.email === "admin@gmail.com"`
- Session persists to localStorage key `"currentUser"`

## API Resources

| Resource | Endpoint    | Key Fields                                                          |
| -------- | ----------- | ------------------------------------------------------------------- |
| Events   | `/events`   | `id`, `slug`, `title`, `date`, `time`, `mode`, `tags[]`, `agenda[]` |
| Users    | `/users`    | `id`, `email`, `password`                                           |
| Bookings | `/bookings` | `id`, `userId`, `eventSlug`, `eventTitle`                           |

Events use `slug` in URLs (`/events/:slug`) but `id` for CRUD operations.

## Developer Workflow

```bash
# Terminal 1: Start JSON Server (from data folder)
cd data && npx json-server --watch db.json --port 3000

# Terminal 2: Start frontend
npm run dev
```

## File Patterns

- **New pages**: Add to `src/pages/`, register route in `App.jsx`
- **New UI components**: Add to `src/components/ui/` using `cn()` utility from `@/lib/utils`
- **Static assets**: Images at `/images/*`, icons at `/icons/*` (from `public/`)

## Notes

- EmailJS credentials hardcoded in `BookEvent.jsx` (SERVICE_ID, TEMPLATE_ID, PUBLIC_KEY)
- `LightRays` component uses Three.js/OGL - heavy WebGL usage
- No TypeScript - uses JSX with jsconfig.json for path resolution
- No testing framework configured
