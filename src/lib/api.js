const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

/**
 * Base fetch wrapper with error handling
 */
async function fetchAPI(endpoint, options = {}) {
  const url = `${API_BASE_URL}${endpoint}`;

  const config = {
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
    ...options,
  };

  try {
    const response = await fetch(url, config);

    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new APIError(
        error.message || `HTTP error! status: ${response.status}`,
        response.status,
        error
      );
    }

    // Handle 204 No Content
    if (response.status === 204) {
      return null;
    }

    return await response.json();
  } catch (error) {
    if (error instanceof APIError) throw error;
    throw new APIError(error.message, 0, null);
  }
}

/**
 * Custom API Error class
 */
export class APIError extends Error {
  constructor(message, status, data) {
    super(message);
    this.name = "APIError";
    this.status = status;
    this.data = data;
  }
}

/**
 * Events API
 */
export const eventsAPI = {
  getAll: () => fetchAPI("/events"),

  getBySlug: (slug) => fetchAPI(`/events/${slug}`),

  create: (eventData) =>
    fetchAPI("/events", {
      method: "POST",
      body: JSON.stringify(eventData),
    }),

  update: (slug, eventData) =>
    fetchAPI(`/events/${slug}`, {
      method: "PUT",
      body: JSON.stringify(eventData),
    }),

  delete: (slug) =>
    fetchAPI(`/events/${slug}`, {
      method: "DELETE",
    }),
};

/**
 * Users API (for future FastAPI migration)
 */
export const usersAPI = {
  getByEmail: (email) => fetchAPI(`/users?email=${encodeURIComponent(email)}`),

  create: (userData) =>
    fetchAPI("/users", {
      method: "POST",
      body: JSON.stringify(userData),
    }),
};

/**
 * Bookings API (for future FastAPI migration)
 */
export const bookingsAPI = {
  getByUserId: (userId) => fetchAPI(`/bookings?userId=${userId}`),

  create: (bookingData) =>
    fetchAPI("/bookings", {
      method: "POST",
      body: JSON.stringify(bookingData),
    }),

  delete: (id) =>
    fetchAPI(`/bookings/${id}`, {
      method: "DELETE",
    }),
};
