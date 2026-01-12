import { useCallback } from "react";
import { eventsAPI } from "@/lib/api";
import { useAPI, useMutation } from "./useAPI";

/**
 * Hook to fetch all events
 */
export function useEvents() {
  return useAPI(eventsAPI.getAll, []);
}

/**
 * Hook to fetch a single event by slug
 */
export function useEvent(slug) {
  const fetchEvent = useCallback(() => eventsAPI.getBySlug(slug), [slug]);
  return useAPI(fetchEvent, [slug], { immediate: !!slug });
}

/**
 * Hook for event mutations with optimistic updates
 */
export function useEventMutations(onSuccess) {
  const createMutation = useMutation(eventsAPI.create);
  const updateMutation = useMutation(eventsAPI.update);
  const deleteMutation = useMutation(eventsAPI.delete);

  const createEvent = async (eventData, optimisticUpdate) => {
    if (optimisticUpdate) optimisticUpdate();
    try {
      const result = await createMutation.mutate(eventData);
      onSuccess?.();
      return result;
    } catch (error) {
      throw error; // Let caller handle rollback
    }
  };

  const updateEvent = async (slug, eventData, optimisticUpdate) => {
    if (optimisticUpdate) optimisticUpdate();
    try {
      const result = await updateMutation.mutate(slug, eventData);
      onSuccess?.();
      return result;
    } catch (error) {
      throw error;
    }
  };

  const deleteEvent = async (slug, optimisticUpdate) => {
    if (optimisticUpdate) optimisticUpdate();
    try {
      const result = await deleteMutation.mutate(slug);
      onSuccess?.();
      return result;
    } catch (error) {
      throw error;
    }
  };

  return {
    createEvent,
    updateEvent,
    deleteEvent,
    isLoading:
      createMutation.loading ||
      updateMutation.loading ||
      deleteMutation.loading,
    error: createMutation.error || updateMutation.error || deleteMutation.error,
  };
}
