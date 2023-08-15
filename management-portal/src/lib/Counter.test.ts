import { fireEvent, render, screen } from '@testing-library/svelte'
import Counter from './Counter.svelte'

describe("Counter", () => {
    it("starts at 0", async () => {
        // Arrange

        // Act
        render(Counter)
        // Assert
        const counter = await screen.findByRole('button')
        expect(counter).toBeTruthy()
        expect(counter.textContent).toBe('count is 0')
    });

    it("increments by 1 when pressed", async () => {
        // Arrange
        render(Counter)
        const counter = await screen.findByRole('button')
        // Act
        await fireEvent.click(counter)
        // Assert
        expect(counter).toBeTruthy()
        expect(counter.textContent).toBe('count is 1')
    });
});

