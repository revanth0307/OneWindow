const countryData = [
  {
    name: "Ireland",
    university: {
      name: "National College Of Ireland",
      location: "Dublin, Ireland",
      ranking: "Ranked top 5%",
      logo:"./images/ireland.png"
    },
    academic_reputation: {
      university_rankings: {
        QS_World_Ranking: "2 universities in the top 200",
        Times_Higher_Education: "3 universities in the top 300"
      },
      accreditation: "Internationally recognized qualifications"
    },
    cost_of_education: {
      tuition_fees: "€10,000 - €25,000 per year"
    },
    living_expenses: {
      cost_of_living: "€9,000 - €12,000 per year"
    }
  },
  {
    name: "UK",
    university: {
      name: "University Of Oxford",
      location: "Oxford, UK",
      ranking: "Ranked top 1%",
      logo: "./images/oxford.png",
       
    },
    academic_reputation: {
      university_rankings: {
        QS_World_Ranking: "4 of the top 10",
        Times_Higher_Education: "3 of the top 10"
      },
      accreditation: "Global recognition and high standards"
    },
    cost_of_education: {
      tuition_fees: "£10,000 - £30,000 per year"
    },
    living_expenses: {
      cost_of_living: "£9,000 - £12,000 per year"
    }
  }
];

export default countryData;
