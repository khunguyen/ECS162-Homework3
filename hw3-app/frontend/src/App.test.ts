import { test, expect, describe, beforeEach, it, vi } from 'vitest';
import { render } from '@testing-library/svelte';
import App from './App.svelte';

test('App', async () =>{
    render(App);
});

// test('should display today date', () => {
//     const { getByTestId } = render(App);
  
//     const currentDateElement = getByTestId('current-date');

//     const today = new Date().toLocaleDateString('en-US', {
//       weekday: 'long',
//       month: 'long',
//       day: 'numeric',
//       year: 'numeric'
//     });
  
//     expect(currentDateElement.textContent).toBe(today);
//   });

  interface Multimedia {
    url: string;
  }

  interface Article {
    title: string;
    url: string;
    abstract: string;
    multimedia: Multimedia;
  }

  const mockData = {
    results: [
      {
        title: 'title',
        url: 'https://www.nytimes.com/mock',
        abstract: 'This is an example abstract.',
        multimedia:
          {
            url: 'https://www.nytimes.com/mock.jpg',
          }
      }
    ]
  };


  test('API data should have expected fields', () => {
    const article: Article = mockData.results[0];
  
    expect(article).toHaveProperty('title');
    expect(article).toHaveProperty('url');
    expect(article).toHaveProperty('abstract');
    expect(article).toHaveProperty('multimedia');
    expect(article.multimedia).toHaveProperty('url');
  });
