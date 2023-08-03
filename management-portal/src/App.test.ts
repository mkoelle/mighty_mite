import {fireEvent, render, screen } from '@testing-library/svelte'
import App from './App.svelte'


describe("Counter", () => {
    test("Should render", async () => {
        // Arrange
        
        // Act
        render(App)
        // Assert
        const header = await screen.findByRole('heading')
        expect(header).toBeTruthy()
        expect(header.textContent).toBe('Mighty Mite')
    });

    test("Should have a counter", async () => {
        // Arrange

        // Act
        render(App)
        // Assert
        const counter = await screen.findByRole('button')
        expect(counter).toBeTruthy()
    });
});

